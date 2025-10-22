import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.01786, 0.0523).lineTo(0.01214, 0.0523).lineTo(0.01214, 0.0023).lineTo(-0.01786, 0.0023).lineTo(-0.01786, 0.0523).close()
solid=wp_sketch0.add(loop0).extrude(-0.05720033273846645)
