import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.04943, 0.03313).lineTo(0.06257, 0.03313).lineTo(0.06257, -0.02487).lineTo(-0.04943, -0.02487).lineTo(-0.04943, 0.03313).close()
solid=wp_sketch0.add(loop0).extrude(0.1630711309487453)
