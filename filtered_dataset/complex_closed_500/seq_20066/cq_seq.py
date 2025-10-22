import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.0, 0.0381).lineTo(0.04445, 0.0381).lineTo(0.05715, 0.01905).lineTo(0.05715, 0.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.04591691849365766)
