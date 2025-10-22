import cadquery as cq
wp_sketch0 = cq.Workplane('XZ')
loop0 = wp_sketch0.moveTo(19.14126, 32.1454).lineTo(19.62327, 32.00387).lineTo(19.98363, 33.23114).lineTo(19.50162, 33.37267).lineTo(19.14126, 32.1454).close()
solid=wp_sketch0.add(loop0).extrude(2.796737262989996)
