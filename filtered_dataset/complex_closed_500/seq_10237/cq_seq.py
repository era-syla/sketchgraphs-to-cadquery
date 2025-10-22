import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.44007, -0.28131).lineTo(0.69615, -0.28131).lineTo(0.69615, -0.0678).lineTo(0.44007, -0.0678).lineTo(0.44007, -0.28131).close()
solid=wp_sketch0.add(loop0).extrude(-0.441763534223299)
