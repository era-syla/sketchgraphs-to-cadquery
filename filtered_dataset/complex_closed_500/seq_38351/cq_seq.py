import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.1338, -0.04396).lineTo(0.13976, -0.04396).lineTo(0.13976, -0.04992).lineTo(0.1338, -0.04992).lineTo(0.1338, -0.04396).close()
solid=wp_sketch0.add(loop0).extrude(-0.015324783278450235)
