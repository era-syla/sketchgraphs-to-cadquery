import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02673, -0.02765).lineTo(0.02673, -0.02765).lineTo(0.02673, 0.02765).lineTo(-0.02673, 0.02765).lineTo(-0.02673, -0.02765).close()
solid=wp_sketch0.add(loop0).extrude(-0.13092051731633464)
