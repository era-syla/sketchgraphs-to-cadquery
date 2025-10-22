import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(-0.0245, -0.0175).lineTo(0.0245, -0.0175).lineTo(0.0245, 0.0175).lineTo(-0.0245, 0.0175).lineTo(-0.0245, -0.0175).close()
solid=wp_sketch0.add(loop0).extrude(-0.0889465580239764)
