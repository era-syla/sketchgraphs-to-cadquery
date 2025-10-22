import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.02915, -0.00301).lineTo(-0.02915, -0.00048).lineTo(-0.02696, -0.00174).lineTo(-0.02915, -0.00301).close()
solid=wp_sketch0.add(loop0).extrude(-0.001532672923141044)
