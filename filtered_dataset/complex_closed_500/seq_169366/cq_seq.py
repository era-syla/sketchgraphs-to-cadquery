import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0375, -0.0375).lineTo(-0.0375, -0.0375).lineTo(-0.0375, 0.0375).lineTo(0.0375, 0.0375).lineTo(0.0375, -0.0375).close()
solid=wp_sketch0.add(loop0).extrude(0.04934515639252592)
