import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.08201, 0.03112).lineTo(0.10131, 0.03112).lineTo(0.10131, 0.0621).lineTo(0.08201, 0.0621).lineTo(0.08201, 0.03112).close()
solid=wp_sketch0.add(loop0).extrude(-0.02884863170838228)
