import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00792, 0.06017).lineTo(-0.00397, 0.04335).lineTo(-0.00397, 0.04157).lineTo(0.00422, 0.04157).lineTo(0.00422, 0.04335).lineTo(0.00807, 0.06014).threePointArc((8e-05, 0.06139), (-0.00792, 0.06017)).close()
solid=wp_sketch0.add(loop0).extrude(-0.029037949203796185)
