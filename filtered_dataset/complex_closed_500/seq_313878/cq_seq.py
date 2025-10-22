import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.14025, 0.09251).lineTo(-0.14025, 0.09251).lineTo(-0.14025, -0.09251).lineTo(0.14025, -0.09251).lineTo(0.14025, 0.09251).close()
solid=wp_sketch0.add(loop0).extrude(0.8410567643419433)
