import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(3.67628, -0.127).lineTo(4.33094, -0.9906).lineTo(5.52426, -0.9906).lineTo(6.17892, -0.127).lineTo(3.67628, -0.127).close()
solid=wp_sketch0.add(loop0).extrude(-0.8024921233407267)
