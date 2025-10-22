import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.004, 0.0042).lineTo(-0.004, 0.0033).lineTo(-0.0031, 0.0033).lineTo(-0.0031, 0.0042).lineTo(-0.004, 0.0042).close()
solid=wp_sketch0.add(loop0).extrude(0.002113037329381923)
