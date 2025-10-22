import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00225, 0.0).lineTo(-0.00225, 0.01).lineTo(-0.0014, 0.01182).lineTo(-0.0014, 0.02032).lineTo(-0.001, 0.02032).lineTo(-0.001, 0.0).lineTo(-0.00225, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.031014171907130118)
