
var dbs = ['db1', 'db2', 'db3', 'db4', 'db5', 'db6', 'db7', 'db8', 'db9']
var A = ['A_100','A_100','A_100', 'A_1000','A_1000','A_1000', 'A_10000', 'A_10000', 'A_10000']
var B = ['B_100_3_0', 'B_100_5_0', 'B_100_10_0', 'B_1000_5_0', 'B_1000_10_1', 'B_1000_50_1','B_10000_5_0', 'B_10000_50_1', 'B_10000_500_1']

// query 4
for(var j = 0;j < 7;j++){
    for(var i = 0;i < 9;i++){
        db = db.getSiblingDB(dbs[i])
        
        db.setProfilingLevel(0)
        db.system.profile.drop()
        db.setProfilingLevel(2)

        c1 = db.B.aggregate([
            {
                $lookup:
                {
                    from:"A",
                    localField:"B2", 
                    foreignField:"A1",
                    as:"new"
                }
            },
            { $unwind:"$new" },
            {
                $project: { "new.A2":1, B1:1, B2:1, B3:1 }
            }
        ]).pretty()

        c2 = db.system.profile.aggregate([ 
            {   
                $match:{
                ns: 
                {
                    $ne : 'db.system.profile' 
                }
            }
        }
        ]).pretty()
        printjson(c2._batch[0])
    }
}
