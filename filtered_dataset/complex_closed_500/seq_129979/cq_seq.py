import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.03023, 0.04483).lineTo(-0.03023, 0.04483).lineTo(-0.03023, -0.04483).lineTo(0.03023, -0.04483).lineTo(0.03023, 0.04483).close()
solid=wp_sketch0.add(loop0).extrude(0.19516450057124438)
