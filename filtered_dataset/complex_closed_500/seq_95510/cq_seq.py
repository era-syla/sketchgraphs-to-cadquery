import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.00257, -0.06102).lineTo(0.11153, -0.06102).lineTo(0.11153, -0.05652).lineTo(0.00257, -0.05652).lineTo(0.00257, -0.06102).close()
solid=wp_sketch0.add(loop0).extrude(-0.16507285646541187)
