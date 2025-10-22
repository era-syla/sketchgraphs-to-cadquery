import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(-0.0069, 0.00148).lineTo(-0.0869, 0.00148).lineTo(-0.0869, 0.00548).lineTo(-0.0069, 0.00548).lineTo(-0.0069, 0.00148).close()
solid=wp_sketch0.add(loop0).extrude(-0.15851055148142865)
