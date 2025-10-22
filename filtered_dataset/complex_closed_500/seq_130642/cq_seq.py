import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.04279, -0.00075).lineTo(0.01595, -0.00075).lineTo(0.01595, 0.00075).lineTo(-0.04279, 0.00075).lineTo(-0.04279, -0.00075).close()
solid=wp_sketch0.add(loop0).extrude(-0.16547630665158672)
