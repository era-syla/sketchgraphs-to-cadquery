import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.001, 0.042).lineTo(-0.001, 0.034).lineTo(-0.007, 0.034).lineTo(-0.007, 0.042).lineTo(-0.001, 0.042).close()
solid=wp_sketch0.add(loop0).extrude(0.006910987214506861)
