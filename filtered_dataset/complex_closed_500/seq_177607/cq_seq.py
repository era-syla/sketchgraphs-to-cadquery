import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0045, -0.012).lineTo(0.0275, -0.012).lineTo(0.0275, 0.0).lineTo(0.0045, 0.0).lineTo(0.0045, -0.012).close()
solid=wp_sketch0.add(loop0).extrude(-0.015247065721914978)
