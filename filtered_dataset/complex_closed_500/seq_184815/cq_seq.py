import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.05612, 0.001).lineTo(0.06812, 0.02673).lineTo(0.06812, 0.001).lineTo(0.05612, 0.001).close()
solid=wp_sketch0.add(loop0).extrude(-0.07275706659547193)
