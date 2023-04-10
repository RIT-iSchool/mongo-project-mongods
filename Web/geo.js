const conn = new Mongo( `mongodb://localhost:27017/` ),
      db   = conn.getDB(  `project`  ),
      coll = db.getCollection( `posts` ),
      geoColl = db.getCollection( `GeoPosts` );
let result;

geoColl.deleteMany({});

coll.find().forEach( doc => {
    geoColl.insertOne( doc );
});

geoColl.updateMany(
    {},
    [{
        $set: { postLoc:{
            $cond: {
                if: {
                    $or: [
                        { $eq: ["$lat",""] },
                        { $eq: ["$lng",""]},
                    ]
                },
                then: null,
                else: {
                    type: `Point`,
                    coordinates: ["$lat","$lng"]
                }
            }
        }}
    }]
);

geoColl.createIndex({ postLoc: '2dsphere' });