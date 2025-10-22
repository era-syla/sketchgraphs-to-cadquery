import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01606, 0.00604).lineTo(0.0661, 0.00604).lineTo(0.0661, 0.19289).lineTo(-0.01606, 0.19289).lineTo(-0.01606, 0.00604).close()
solid=wp_sketch0.add(loop0).extrude(-0.24191836875919287)
