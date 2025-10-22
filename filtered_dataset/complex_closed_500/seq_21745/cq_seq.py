import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.05974, 0.0688).lineTo(0.04026, 0.0688).lineTo(0.04026, 0.0288).lineTo(-0.05974, 0.0288).lineTo(-0.05974, 0.0688).close()
solid=wp_sketch0.add(loop0).extrude(-0.2139891118143643)
