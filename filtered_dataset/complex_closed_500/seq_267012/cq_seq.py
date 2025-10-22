import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.06398, -0.06491).lineTo(-0.06398, -0.06491).lineTo(-0.06398, 0.06491).lineTo(0.06398, 0.06491).lineTo(0.06398, -0.06491).close()
solid=wp_sketch0.add(loop0).extrude(0.13458492685462212)
