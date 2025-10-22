import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.3041, 0.0035).lineTo(0.31364, 0.0035).lineTo(0.31364, -0.00093).lineTo(0.3041, -0.00093).lineTo(0.29914, 0.0035).lineTo(0.3041, 0.0035).close()
solid=wp_sketch0.add(loop0).extrude(-0.017742541301267428)
