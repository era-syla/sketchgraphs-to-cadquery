import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.013).lineTo(0.00575, 0.013).lineTo(0.00575, 0.017).lineTo(-0.02825, 0.017).lineTo(-0.02825, 0.013).lineTo(0.0, 0.013).close()
solid=wp_sketch0.add(loop0).extrude(0.06397928377286051)
