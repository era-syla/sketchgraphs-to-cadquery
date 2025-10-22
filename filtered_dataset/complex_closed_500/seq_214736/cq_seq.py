import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0, 0.0).lineTo(0.042, 0.0).lineTo(0.042, 0.0185).lineTo(0.0, 0.0185).lineTo(0.0, 0.0).close()
solid=wp_sketch0.add(loop0).extrude(0.033348670319438355)
