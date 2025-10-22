import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.30257, -0.07498).lineTo(0.70597, -0.07498).lineTo(0.70597, -0.49037).lineTo(-0.30257, -0.49037).lineTo(-0.30257, -0.07498).close()
solid=wp_sketch0.add(loop0).extrude(1.9798586446113926)
