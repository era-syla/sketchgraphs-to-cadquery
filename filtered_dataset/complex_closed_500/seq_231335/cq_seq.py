import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.015, -0.00523).lineTo(0.015, -0.00523).lineTo(0.015, -0.03523).lineTo(-0.015, -0.03523).lineTo(-0.015, -0.00523).close()
solid=wp_sketch0.add(loop0).extrude(0.06980110723797359)
