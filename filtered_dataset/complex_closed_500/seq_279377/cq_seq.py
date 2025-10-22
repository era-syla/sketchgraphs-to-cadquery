import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.025).lineTo(-0.003, 0.025).lineTo(-0.003, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.025).close()
solid=wp_sketch0.add(loop0).extrude(0.05536700012175686)
