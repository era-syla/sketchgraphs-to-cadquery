import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.12729, 0.06599).lineTo(-0.01621, 0.06599).lineTo(-0.01621, 0.01893).lineTo(-0.1265, 0.01893).lineTo(-0.12729, 0.06599).close()
solid=wp_sketch0.add(loop0).extrude(0.10455710204861991)
