import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(20.0, 0.0).lineTo(20.0, -15.0).lineTo(0.0, -15.0).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(-55.237551840149436)
