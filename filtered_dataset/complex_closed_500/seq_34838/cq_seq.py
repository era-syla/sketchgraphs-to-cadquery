import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-16.90933, 61.591).lineTo(-12.90933, 61.591).lineTo(-12.90933, 2.8457).lineTo(-16.90933, 2.8457).lineTo(-16.90933, 61.591).close()
solid=wp_sketch0.add(loop0).extrude(-102.2897997504824)
