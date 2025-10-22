import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.10478, -0.00556).lineTo(0.10795, -0.00556).lineTo(0.10795, -0.01117).lineTo(0.10478, -0.01117).lineTo(0.10478, -0.00556).close()
solid=wp_sketch0.add(loop0).extrude(0.01151721711526352)
