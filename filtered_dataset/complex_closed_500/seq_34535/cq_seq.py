import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0058, 0.03).lineTo(0.0038, 0.03).lineTo(0.0038, -0.0035).lineTo(0.0058, -0.0035).lineTo(0.0058, 0.03).close()
solid=wp_sketch0.add(loop0).extrude(-0.044315321723550516)
