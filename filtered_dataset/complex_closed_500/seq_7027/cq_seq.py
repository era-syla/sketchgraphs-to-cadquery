import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.00635, 0.0).lineTo(-0.00635, 0.031).lineTo(-0.0175, 0.031).lineTo(-0.0175, 0.021).lineTo(-0.0275, 0.021).lineTo(-0.0275, 0.0185).lineTo(-0.02546, 0.0185).lineTo(-0.02546, 0.0025).lineTo(-0.0275, 0.0025).lineTo(-0.0275, 0.0).lineTo(-0.00635, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-0.09262659165977072)
