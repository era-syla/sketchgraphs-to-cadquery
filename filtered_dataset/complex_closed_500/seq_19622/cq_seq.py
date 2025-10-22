import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.01589, 0.07961).lineTo(0.01289, 0.07961).lineTo(0.01289, 0.07461).lineTo(0.01589, 0.07461).lineTo(0.01589, 0.07961).close()
solid=wp_sketch0.add(loop0).extrude(-0.012159140599093255)
