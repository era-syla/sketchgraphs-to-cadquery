import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05177, -0.05796).lineTo(-0.15177, -0.05796).lineTo(-0.15177, -0.03796).lineTo(-0.05177, -0.03796).lineTo(-0.05177, -0.05796).close()
solid=wp_sketch0.add(loop0).extrude(-0.28976365934741216)
