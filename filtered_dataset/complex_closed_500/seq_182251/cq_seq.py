import cadquery as cq
wp_sketch0 = cq.Workplane('XY')
loop0 = wp_sketch0.moveTo(0.0085, 0.0133).lineTo(0.0085, 0.005).lineTo(0.0125, 0.005).lineTo(0.0125, 0.0).lineTo(0.0, 0.0).lineTo(0.0, 0.0133).lineTo(0.0085, 0.0133).close()
solid=wp_sketch0.add(loop0).extrude(0.01678863477750102)
