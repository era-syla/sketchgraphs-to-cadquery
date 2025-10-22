import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.075, -0.17542).lineTo(-0.075, -0.17542).lineTo(-0.075, 0.17542).lineTo(0.075, 0.17542).lineTo(0.075, -0.17542).close()
solid=wp_sketch0.add(loop0).extrude(0.31515253144249666)
