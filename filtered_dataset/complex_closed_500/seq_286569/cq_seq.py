import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.004, -0.0212).lineTo(0.004, -0.0212).lineTo(0.004, 0.00284).lineTo(-0.004, 0.00284).lineTo(-0.004, -0.0212).close()
solid=wp_sketch0.add(loop0).extrude(0.05279703932798506)
