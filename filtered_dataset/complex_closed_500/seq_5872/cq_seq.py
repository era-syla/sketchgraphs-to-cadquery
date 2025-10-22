import cadquery as cq
wp_sketch0 = cq.Workplane('YZ')
loop0 = wp_sketch0.moveTo(-0.02642, 0.012).lineTo(-0.02842, 0.012).lineTo(-0.02842, 0.00902).threePointArc((-0.02967, 0.007), (-0.02842, 0.00498)).lineTo(-0.02842, 0.002).lineTo(-0.02642, 0.002).lineTo(-0.02642, 0.00498).threePointArc((-0.02517, 0.007), (-0.02642, 0.00902)).lineTo(-0.02642, 0.012).close()
solid=wp_sketch0.add(loop0).extrude(0.007541022053041222)
