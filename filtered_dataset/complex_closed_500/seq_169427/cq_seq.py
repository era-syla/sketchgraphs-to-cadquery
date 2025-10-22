import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00022, 0.00475).lineTo(0.00142, 0.00475).lineTo(0.00142, 0.00565).lineTo(0.00022, 0.00565).lineTo(0.00022, 0.00475).close()
solid=wp_sketch0.add(loop0).extrude(4.069014650646601e-05)
