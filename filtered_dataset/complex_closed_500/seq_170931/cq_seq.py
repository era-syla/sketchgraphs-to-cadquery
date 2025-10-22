import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(0.00952, 0.10478).lineTo(0.34608, 0.10478).lineTo(0.34608, 0.20002).lineTo(0.00952, 0.20002).lineTo(0.00952, 0.10478).close()
solid=wp_sketch0.add(loop0).extrude(0.3388983383630901)
