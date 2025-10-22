import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0084, -0.00535).lineTo(-0.0084, -0.00535).lineTo(-0.0084, -0.01035).lineTo(0.0084, -0.01035).lineTo(0.0084, -0.00535).close()
solid=wp_sketch0.add(loop0).extrude(-0.03141588434390566)
