import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(0.01134, -0.03636).lineTo(-0.01134, -0.03636).lineTo(-0.01134, -0.01921).lineTo(0.01134, -0.01921).lineTo(0.01134, -0.03636).close()
solid=wp_sketch0.add(loop0).extrude(0.010909631256387135)
