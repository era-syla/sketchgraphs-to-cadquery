import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.02371, 0.12067).lineTo(0.08193, 0.12067).lineTo(0.08193, 0.09233).lineTo(0.02371, 0.09233).lineTo(0.02371, 0.12067).close()
solid=wp_sketch0.add(loop0).extrude(-0.07423251822944081)
