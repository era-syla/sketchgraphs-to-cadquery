import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0825, 0.00475).lineTo(-0.0825, 0.00375).lineTo(-0.0845, 0.0035).lineTo(-0.0925, 0.0035).lineTo(-0.0825, 0.00475).close()
solid=wp_sketch0.add(loop0).extrude(0.023963786141039604)
