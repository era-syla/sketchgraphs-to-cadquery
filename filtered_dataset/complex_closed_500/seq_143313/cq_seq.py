import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.03235, -0.006).lineTo(0.1146, -0.006).lineTo(0.1146, 0.02735).lineTo(-0.03235, 0.02735).lineTo(-0.03235, -0.006).close()
solid=wp_sketch0.add(loop0).extrude(0.21910646230683264)
