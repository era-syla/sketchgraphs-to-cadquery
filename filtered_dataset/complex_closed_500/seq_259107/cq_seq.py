import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-1.01391, 0.20589).lineTo(0.67609, 0.20589).lineTo(0.67609, -0.16411).lineTo(-1.01391, -0.28411).lineTo(-1.01391, 0.20589).close()
solid=wp_sketch0.add(loop0).extrude(0.8593734060880917)
